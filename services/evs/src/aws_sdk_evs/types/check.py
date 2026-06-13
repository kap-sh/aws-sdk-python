"""Generated from Smithy shape ``com.amazonaws.evs#Check``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_evs.types.check_result
    import aws_sdk_evs.types.check_type


class Check(TypedDict):
    type: NotRequired["aws_sdk_evs.types.check_type.CheckType"]
    """<p>The check type. Amazon EVS performs the following checks.</p> <ul> <li> <p> <code>KEY_REUSE</code>: checks that the VCF license key is not used by another Amazon EVS environment. This check fails if a used license is added to the environment.</p> </li> <li> <p> <code>KEY_COVERAGE</code>: checks that your VCF license key allocates sufficient vCPU cores for all deployed hosts. The check fails when any assigned hosts in the EVS environment are not covered by license keys, or when any unassigned hosts cannot be covered by available vCPU cores in keys.</p> </li> <li> <p> <code>REACHABILITY</code>: checks that the Amazon EVS control plane has a persistent connection to SDDC Manager. If Amazon EVS cannot reach the environment, this check fails.</p> </li> <li> <p> <code>HOST_COUNT</code>: Checks that your environment has a minimum of 4 hosts.</p> <p>If this check fails, you will need to add hosts so that your environment meets this minimum requirement. Amazon EVS only supports environments with 4-32 hosts.</p> </li> </ul>"""
    result: NotRequired["aws_sdk_evs.types.check_result.CheckResult"]
    """<p> The check result.</p>"""
    impaired_since: NotRequired["datetime.datetime"]
    """<p>The time when environment health began to be impaired.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Check) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_evs.types.check_type

        out["type"] = aws_sdk_evs.types.check_type.serialize_aws_json_1_0(value["type"])
    if "result" in value:
        import aws_sdk_evs.types.check_result

        out["result"] = aws_sdk_evs.types.check_result.serialize_aws_json_1_0(
            value["result"]
        )
    if "impaired_since" in value:
        import aws_sdk_evs.types._prelude.timestamp

        out["impairedSince"] = (
            aws_sdk_evs.types._prelude.timestamp.serialize_aws_json_1_0(
                value["impaired_since"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Check:
    out: Check = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_evs.types.check_type

        out["type"] = aws_sdk_evs.types.check_type.deserialize_aws_json_1_0(
            data["type"]
        )
    if "result" in data:
        import aws_sdk_evs.types.check_result

        out["result"] = aws_sdk_evs.types.check_result.deserialize_aws_json_1_0(
            data["result"]
        )
    if "impairedSince" in data:
        import aws_sdk_evs.types._prelude.timestamp

        out["impaired_since"] = (
            aws_sdk_evs.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["impairedSince"]
            )
        )
    return out
