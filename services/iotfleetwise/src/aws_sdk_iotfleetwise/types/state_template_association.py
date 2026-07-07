"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StateTemplateAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.resource_identifier
    import aws_sdk_iotfleetwise.types.state_template_update_strategy


class StateTemplateAssociation(TypedDict, closed=True):
    identifier: "aws_sdk_iotfleetwise.types.resource_identifier.ResourceIdentifier"
    """<p>The unique ID of the state template.</p>"""
    state_template_update_strategy: "aws_sdk_iotfleetwise.types.state_template_update_strategy.StateTemplateUpdateStrategy"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StateTemplateAssociation) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    import aws_sdk_iotfleetwise.types.state_template_update_strategy

    out["stateTemplateUpdateStrategy"] = (
        aws_sdk_iotfleetwise.types.state_template_update_strategy.serialize_aws_json_1_0(
            value["state_template_update_strategy"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> StateTemplateAssociation:
    out: StateTemplateAssociation = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("StateTemplateAssociation.identifier required")
    if "stateTemplateUpdateStrategy" in data:
        import aws_sdk_iotfleetwise.types.state_template_update_strategy

        out["state_template_update_strategy"] = (
            aws_sdk_iotfleetwise.types.state_template_update_strategy.deserialize_aws_json_1_0(
                data["stateTemplateUpdateStrategy"]
            )
        )
    else:
        raise DeserializationError(
            "StateTemplateAssociation.state_template_update_strategy required"
        )
    return out
