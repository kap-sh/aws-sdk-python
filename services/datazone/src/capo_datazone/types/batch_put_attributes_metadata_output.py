"""Generated from Smithy shape ``com.amazonaws.datazone#BatchPutAttributesMetadataOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.attributes_errors
    import capo_datazone.types.batch_put_attribute_items


class BatchPutAttributesMetadataOutput(TypedDict, closed=True):
    errors: NotRequired["capo_datazone.types.attributes_errors.AttributesErrors"]
    """<p>The errors generated when the BatchPutAttributeMetadata action is invoked.</p>"""
    attributes: NotRequired[
        "capo_datazone.types.batch_put_attribute_items.BatchPutAttributeItems"
    ]
    """<p>The results of the BatchPutAttributeMetadata action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutAttributesMetadataOutput) -> dict:
    out: dict = {}
    if "errors" in value:
        import capo_datazone.types.attributes_errors

        out["errors"] = capo_datazone.types.attributes_errors.serialize_json(
            value["errors"]
        )
    if "attributes" in value:
        import capo_datazone.types.batch_put_attribute_items

        out["attributes"] = (
            capo_datazone.types.batch_put_attribute_items.serialize_json(
                value["attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchPutAttributesMetadataOutput:
    out: BatchPutAttributesMetadataOutput = {}  # type: ignore[typeddict-item]
    if "errors" in data:
        import capo_datazone.types.attributes_errors

        out["errors"] = capo_datazone.types.attributes_errors.deserialize_json(
            data["errors"]
        )
    if "attributes" in data:
        import capo_datazone.types.batch_put_attribute_items

        out["attributes"] = (
            capo_datazone.types.batch_put_attribute_items.deserialize_json(
                data["attributes"]
            )
        )
    return out
