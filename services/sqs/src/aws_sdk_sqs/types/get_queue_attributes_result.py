"""Generated from Smithy shape ``com.amazonaws.sqs#GetQueueAttributesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sqs.types.queue_attribute_map


class GetQueueAttributesResult(TypedDict):
    attributes: NotRequired["aws_sdk_sqs.types.queue_attribute_map.QueueAttributeMap"]
    """<p>A map of attributes to their respective values.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetQueueAttributesResult) -> dict:
    out: dict = {}
    if "attributes" in value:
        import aws_sdk_sqs.types.queue_attribute_map

        out["Attributes"] = (
            aws_sdk_sqs.types.queue_attribute_map.serialize_aws_json_1_0(
                value["attributes"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetQueueAttributesResult:
    out: GetQueueAttributesResult = {}  # type: ignore[typeddict-item]
    if "Attributes" in data:
        import aws_sdk_sqs.types.queue_attribute_map

        out["attributes"] = (
            aws_sdk_sqs.types.queue_attribute_map.deserialize_aws_json_1_0(
                data["Attributes"]
            )
        )
    return out
