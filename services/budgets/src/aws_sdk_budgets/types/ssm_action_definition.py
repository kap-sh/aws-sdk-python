"""Generated from Smithy shape ``com.amazonaws.budgets#SsmActionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_budgets.types.action_sub_type
    import aws_sdk_budgets.types.instance_ids
    import aws_sdk_budgets.types.region


class SsmActionDefinition(TypedDict, closed=True):
    action_sub_type: "aws_sdk_budgets.types.action_sub_type.ActionSubType"
    """<p>The action subType. </p>"""
    region: "aws_sdk_budgets.types.region.Region"
    """<p>The Region to run the SSM document. </p>"""
    instance_ids: "aws_sdk_budgets.types.instance_ids.InstanceIds"
    """<p>The EC2 and RDS instance IDs. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SsmActionDefinition) -> dict:
    out: dict = {}
    import aws_sdk_budgets.types.action_sub_type

    out["ActionSubType"] = aws_sdk_budgets.types.action_sub_type.serialize_aws_json_1_1(
        value["action_sub_type"]
    )
    out["Region"] = value["region"]
    import aws_sdk_budgets.types.instance_ids

    out["InstanceIds"] = aws_sdk_budgets.types.instance_ids.serialize_aws_json_1_1(
        value["instance_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SsmActionDefinition:
    out: SsmActionDefinition = {}  # type: ignore[typeddict-item]
    if "ActionSubType" in data:
        import aws_sdk_budgets.types.action_sub_type

        out["action_sub_type"] = (
            aws_sdk_budgets.types.action_sub_type.deserialize_aws_json_1_1(
                data["ActionSubType"]
            )
        )
    else:
        raise DeserializationError("SsmActionDefinition.action_sub_type required")
    if "Region" in data:
        out["region"] = data["Region"]
    else:
        raise DeserializationError("SsmActionDefinition.region required")
    if "InstanceIds" in data:
        import aws_sdk_budgets.types.instance_ids

        out["instance_ids"] = (
            aws_sdk_budgets.types.instance_ids.deserialize_aws_json_1_1(
                data["InstanceIds"]
            )
        )
    else:
        raise DeserializationError("SsmActionDefinition.instance_ids required")
    return out
