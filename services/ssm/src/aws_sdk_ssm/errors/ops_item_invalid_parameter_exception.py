"""Generated from Smithy shape ``com.amazonaws.ssm#OpsItemInvalidParameterException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.ops_item_parameter_names_list
    import aws_sdk_ssm.types.string


class OpsItemInvalidParameterException_(TypedDict, closed=True):
    parameter_names: NotRequired[
        "aws_sdk_ssm.types.ops_item_parameter_names_list.OpsItemParameterNamesList"
    ]
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsItemInvalidParameterException_) -> dict:
    out: dict = {}
    if "parameter_names" in value:
        import aws_sdk_ssm.types.ops_item_parameter_names_list

        out["ParameterNames"] = (
            aws_sdk_ssm.types.ops_item_parameter_names_list.serialize_aws_json_1_1(
                value["parameter_names"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsItemInvalidParameterException_:
    out: OpsItemInvalidParameterException_ = {}  # type: ignore[typeddict-item]
    if "ParameterNames" in data:
        import aws_sdk_ssm.types.ops_item_parameter_names_list

        out["parameter_names"] = (
            aws_sdk_ssm.types.ops_item_parameter_names_list.deserialize_aws_json_1_1(
                data["ParameterNames"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class OpsItemInvalidParameterException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#OpsItemInvalidParameterException``."""

    code: str | None = "OpsItemInvalidParameterException"

    def __init__(self, data: OpsItemInvalidParameterException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OpsItemInvalidParameterException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "OpsItemInvalidParameterException":
        return cls(deserialize_aws_json_1_1(data))
