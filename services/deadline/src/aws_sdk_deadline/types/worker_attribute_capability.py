"""Generated from Smithy shape ``com.amazonaws.deadline#WorkerAttributeCapability``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.attribute_capability_name
    import aws_sdk_deadline.types.attribute_capability_values_list


class WorkerAttributeCapability(TypedDict):
    name: "aws_sdk_deadline.types.attribute_capability_name.AttributeCapabilityName"
    """<p>The name of the worker attribute capability.</p>"""
    values: "aws_sdk_deadline.types.attribute_capability_values_list.AttributeCapabilityValuesList"
    """<p>The values of the worker amount capability.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerAttributeCapability) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_deadline.types.attribute_capability_values_list

    out["values"] = (
        aws_sdk_deadline.types.attribute_capability_values_list.serialize_json(
            value["values"]
        )
    )
    return out


def deserialize_json(data: dict) -> WorkerAttributeCapability:
    out: WorkerAttributeCapability = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("WorkerAttributeCapability.name required")
    if "values" in data:
        import aws_sdk_deadline.types.attribute_capability_values_list

        out["values"] = (
            aws_sdk_deadline.types.attribute_capability_values_list.deserialize_json(
                data["values"]
            )
        )
    else:
        raise DeserializationError("WorkerAttributeCapability.values required")
    return out
