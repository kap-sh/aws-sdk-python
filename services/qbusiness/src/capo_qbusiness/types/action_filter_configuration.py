"""Generated from Smithy shape ``com.amazonaws.qbusiness#ActionFilterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.attribute_filter


class ActionFilterConfiguration(TypedDict, closed=True):
    document_attribute_filter: "capo_qbusiness.types.attribute_filter.AttributeFilter"


# --- restJson1 ser/de ---
def serialize_json(value: ActionFilterConfiguration) -> dict:
    out: dict = {}
    import capo_qbusiness.types.attribute_filter

    out["documentAttributeFilter"] = (
        capo_qbusiness.types.attribute_filter.serialize_json(
            value["document_attribute_filter"]
        )
    )
    return out


def deserialize_json(data: dict) -> ActionFilterConfiguration:
    out: ActionFilterConfiguration = {}  # type: ignore[typeddict-item]
    if "documentAttributeFilter" in data:
        import capo_qbusiness.types.attribute_filter

        out["document_attribute_filter"] = (
            capo_qbusiness.types.attribute_filter.deserialize_json(
                data["documentAttributeFilter"]
            )
        )
    else:
        raise DeserializationError(
            "ActionFilterConfiguration.document_attribute_filter required"
        )
    return out
