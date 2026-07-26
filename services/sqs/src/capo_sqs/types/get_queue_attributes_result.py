"""Generated from Smithy shape ``com.amazonaws.sqs#GetQueueAttributesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.queue_attribute_map


class GetQueueAttributesResult(TypedDict, closed=True):
    attributes: NotRequired["capo_sqs.types.queue_attribute_map.QueueAttributeMap"]
    """<p>A map of attributes to their respective values.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetQueueAttributesResult) -> dict:
    out: dict = {}
    if "attributes" in value:
        import capo_sqs.types.queue_attribute_map

        out["Attributes"] = capo_sqs.types.queue_attribute_map.serialize_aws_json_1_0(
            value["attributes"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetQueueAttributesResult:
    out: GetQueueAttributesResult = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import capo_sqs.types.queue_attribute_map

        out["attributes"] = capo_sqs.types.queue_attribute_map.deserialize_aws_json_1_0(
            data["Attributes"]
        )
    return out
