"""Generated from Smithy shape ``com.amazonaws.ssm#InstancePatchStateFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.instance_patch_state_filter_key
    import aws_sdk_ssm.types.instance_patch_state_filter_values
    import aws_sdk_ssm.types.instance_patch_state_operator_type


class InstancePatchStateFilter(TypedDict, closed=True):
    key: "aws_sdk_ssm.types.instance_patch_state_filter_key.InstancePatchStateFilterKey"
    """<p>The key for the filter. Supported values include the following:</p> <ul> <li> <p> <code>InstalledCount</code> </p> </li> <li> <p> <code>InstalledOtherCount</code> </p> </li> <li> <p> <code>InstalledPendingRebootCount</code> </p> </li> <li> <p> <code>InstalledRejectedCount</code> </p> </li> <li> <p> <code>MissingCount</code> </p> </li> <li> <p> <code>FailedCount</code> </p> </li> <li> <p> <code>UnreportedNotApplicableCount</code> </p> </li> <li> <p> <code>NotApplicableCount</code> </p> </li> </ul>"""
    values: "aws_sdk_ssm.types.instance_patch_state_filter_values.InstancePatchStateFilterValues"
    """<p>The value for the filter. Must be an integer greater than or equal to 0.</p>"""
    type: "aws_sdk_ssm.types.instance_patch_state_operator_type.InstancePatchStateOperatorType"
    """<p>The type of comparison that should be performed for the value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePatchStateFilter) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    import aws_sdk_ssm.types.instance_patch_state_filter_values

    out["Values"] = (
        aws_sdk_ssm.types.instance_patch_state_filter_values.serialize_aws_json_1_1(
            value["values"]
        )
    )
    import aws_sdk_ssm.types.instance_patch_state_operator_type

    out["Type"] = (
        aws_sdk_ssm.types.instance_patch_state_operator_type.serialize_aws_json_1_1(
            value["type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstancePatchStateFilter:
    out: InstancePatchStateFilter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("InstancePatchStateFilter.key required")
    if "Values" in data:
        import aws_sdk_ssm.types.instance_patch_state_filter_values

        out["values"] = (
            aws_sdk_ssm.types.instance_patch_state_filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("InstancePatchStateFilter.values required")
    if "Type" in data:
        import aws_sdk_ssm.types.instance_patch_state_operator_type

        out["type"] = (
            aws_sdk_ssm.types.instance_patch_state_operator_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("InstancePatchStateFilter.type required")
    return out
