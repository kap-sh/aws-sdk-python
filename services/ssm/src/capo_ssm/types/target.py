"""Generated from Smithy shape ``com.amazonaws.ssm#Target``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.target_key
    import capo_ssm.types.target_values


class Target(TypedDict, closed=True):
    key: NotRequired["capo_ssm.types.target_key.TargetKey"]
    """<p>User-defined criteria for sending commands that target managed nodes that meet the criteria.</p>"""
    values: NotRequired["capo_ssm.types.target_values.TargetValues"]
    """<p>User-defined criteria that maps to <code>Key</code>. For example, if you specified <code>tag:ServerRole</code>, you could specify <code>value:WebServer</code> to run a command on instances that include EC2 tags of <code>ServerRole,WebServer</code>. </p> <p>Depending on the type of target, the maximum number of values for a key might be lower than the global maximum of 50.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Target) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "values" in value:
        import capo_ssm.types.target_values

        out["Values"] = capo_ssm.types.target_values.serialize_aws_json_1_1(
            value["values"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Target:
    out: Target = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Values" in data:
        import capo_ssm.types.target_values

        out["values"] = capo_ssm.types.target_values.deserialize_aws_json_1_1(
            data["Values"]
        )
    return out
