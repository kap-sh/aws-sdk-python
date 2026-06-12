"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#UpdateLabelGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.fault_codes
    import aws_sdk_lookoutequipment.types.label_group_name


class UpdateLabelGroupRequest(TypedDict):
    label_group_name: "aws_sdk_lookoutequipment.types.label_group_name.LabelGroupName"
    """<p> The name of the label group to be updated. </p>"""
    fault_codes: NotRequired["aws_sdk_lookoutequipment.types.fault_codes.FaultCodes"]
    """<p> Updates the code indicating the type of anomaly associated with the label. </p> <p>Data in this field will be retained for service usage. Follow best practices for the security of your data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateLabelGroupRequest) -> dict:
    out: dict = {}
    out["LabelGroupName"] = value["label_group_name"]
    if "fault_codes" in value:
        import aws_sdk_lookoutequipment.types.fault_codes

        out["FaultCodes"] = (
            aws_sdk_lookoutequipment.types.fault_codes.serialize_aws_json_1_0(
                value["fault_codes"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateLabelGroupRequest:
    out: UpdateLabelGroupRequest = {}  # type: ignore[typeddict-item]
    if "LabelGroupName" in data:
        out["label_group_name"] = data["LabelGroupName"]
    else:
        raise DeserializationError("UpdateLabelGroupRequest.label_group_name required")
    if "FaultCodes" in data:
        import aws_sdk_lookoutequipment.types.fault_codes

        out["fault_codes"] = (
            aws_sdk_lookoutequipment.types.fault_codes.deserialize_aws_json_1_0(
                data["FaultCodes"]
            )
        )
    return out
