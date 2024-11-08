/* eslint-disable */

import plugin from "tailwindcss/plugin";

export default {
    mode: "jit",
    darkMode: "media",
    future: {
        removeDeprecatedGapUtilities: true,
        purgeLayersByDefault: true,
    },
    content: ["./templates/**/*.html"],
    safelist: [
        "message-error",
        "message-info",
        "message-success",
        "message-warning",
        "btn-danger",
        "btn-default",
        "btn-primary",
    ],
    keyframes: true,
    variants: {
        padding: ["first", "last"],
        textColor: ["responsive", "hover", "focus", "visited", "dark"],
    },
    plugins: [
        // https://www.crocodile.dev/blog/css-transitions-with-tailwind-and-htmx
        plugin(function ({ addVariant }) {
            addVariant("htmx-settling", [
                "&.htmx-settling",
                ".htmx-settling &",
            ]);
            addVariant("htmx-request", ["&.htmx-request", ".htmx-request &"]);
            addVariant("htmx-swapping", [
                "&.htmx-swapping",
                ".htmx-swapping &",
            ]);
            addVariant("htmx-added", ["&.htmx-added", ".htmx-added &"]);
        }),
        require("@tailwindcss/forms", {
            strategy: "class",
        }),
        require("@tailwindcss/typography"),
    ],
    theme: {
        extend: {
            spacing: {
                128: "32rem",
            },
        },
    },
};
