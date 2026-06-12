"""Generated from Smithy shape ``com.amazonaws.deadline#WorkerCapabilities``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.worker_amount_capability_list
    import aws_sdk_deadline.types.worker_attribute_capability_list


class WorkerCapabilities(TypedDict):
    amounts: "aws_sdk_deadline.types.worker_amount_capability_list.WorkerAmountCapabilityList"
    """<p>The worker capabilities amounts on a list of worker capabilities.</p>"""
    attributes: "aws_sdk_deadline.types.worker_attribute_capability_list.WorkerAttributeCapabilityList"
    """<p>The worker attribute capabilities in the list of attribute capabilities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerCapabilities) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.worker_amount_capability_list

    out["amounts"] = (
        aws_sdk_deadline.types.worker_amount_capability_list.serialize_json(
            value["amounts"]
        )
    )
    import aws_sdk_deadline.types.worker_attribute_capability_list

    out["attributes"] = (
        aws_sdk_deadline.types.worker_attribute_capability_list.serialize_json(
            value["attributes"]
        )
    )
    return out


def deserialize_json(data: dict) -> WorkerCapabilities:
    out: WorkerCapabilities = {}  # type: ignore[typeddict-item]
    if "amounts" in data:
        import aws_sdk_deadline.types.worker_amount_capability_list

        out["amounts"] = (
            aws_sdk_deadline.types.worker_amount_capability_list.deserialize_json(
                data["amounts"]
            )
        )
    else:
        raise DeserializationError("WorkerCapabilities.amounts required")
    if "attributes" in data:
        import aws_sdk_deadline.types.worker_attribute_capability_list

        out["attributes"] = (
            aws_sdk_deadline.types.worker_attribute_capability_list.deserialize_json(
                data["attributes"]
            )
        )
    else:
        raise DeserializationError("WorkerCapabilities.attributes required")
    return out
