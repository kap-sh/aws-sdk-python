"""Generated from Smithy shape ``com.amazonaws.sqs#QueueAttributeMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sqs.types.queue_attribute_name
    import capo_sqs.types.string

QueueAttributeMap: TypeAlias = dict[
    "capo_sqs.types.queue_attribute_name.QueueAttributeName",
    "capo_sqs.types.string.String",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: QueueAttributeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_sqs.types.queue_attribute_name

        out[capo_sqs.types.queue_attribute_name.serialize_aws_json_1_0(key)] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> QueueAttributeMap:
    out: QueueAttributeMap = {}
    for key, value in data.items():
        import capo_sqs.types.queue_attribute_name

        if value is None:
            continue
        out[capo_sqs.types.queue_attribute_name.deserialize_aws_json_1_0(key)] = value
    return out
