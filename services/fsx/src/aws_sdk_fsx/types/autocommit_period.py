"""Generated from Smithy shape ``com.amazonaws.fsx#AutocommitPeriod``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.autocommit_period_type
    import aws_sdk_fsx.types.autocommit_period_value


class AutocommitPeriod(TypedDict):
    type: NotRequired["aws_sdk_fsx.types.autocommit_period_type.AutocommitPeriodType"]
    """<p>Defines the type of time for the autocommit period of a file in an FSx for ONTAP SnapLock volume. Setting this value to <code>NONE</code> disables autocommit. The default value is <code>NONE</code>. </p>"""
    value: NotRequired[
        "aws_sdk_fsx.types.autocommit_period_value.AutocommitPeriodValue"
    ]
    """<p>Defines the amount of time for the autocommit period of a file in an FSx for ONTAP SnapLock volume. The following ranges are valid: </p> <ul> <li> <p> <code>Minutes</code>: 5 - 65,535</p> </li> <li> <p> <code>Hours</code>: 1 - 65,535</p> </li> <li> <p> <code>Days</code>: 1 - 3,650</p> </li> <li> <p> <code>Months</code>: 1 - 120</p> </li> <li> <p> <code>Years</code>: 1 - 10</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutocommitPeriod) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_fsx.types.autocommit_period_type

        out["Type"] = aws_sdk_fsx.types.autocommit_period_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AutocommitPeriod:
    out: AutocommitPeriod = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_fsx.types.autocommit_period_type

        out["type"] = aws_sdk_fsx.types.autocommit_period_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "Value" in data:
        out["value"] = data["Value"]
    return out
