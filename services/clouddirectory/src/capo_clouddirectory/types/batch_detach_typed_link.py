"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchDetachTypedLink``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.typed_link_specifier


class BatchDetachTypedLink(TypedDict, closed=True):
    typed_link_specifier: (
        "capo_clouddirectory.types.typed_link_specifier.TypedLinkSpecifier"
    )
    """<p>Used to accept a typed link specifier as input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDetachTypedLink) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.typed_link_specifier

    out["TypedLinkSpecifier"] = (
        capo_clouddirectory.types.typed_link_specifier.serialize_json(
            value["typed_link_specifier"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDetachTypedLink:
    out: BatchDetachTypedLink = {}  # type: ignore[typeddict-item]
    if "TypedLinkSpecifier" in data:
        import capo_clouddirectory.types.typed_link_specifier

        out["typed_link_specifier"] = (
            capo_clouddirectory.types.typed_link_specifier.deserialize_json(
                data["TypedLinkSpecifier"]
            )
        )
    else:
        raise DeserializationError("BatchDetachTypedLink.typed_link_specifier required")
    return out
