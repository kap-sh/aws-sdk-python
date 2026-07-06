"""Generated from Smithy shape ``com.amazonaws.dlm#InvalidRequestException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dlm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dlm.types.error_code
    import aws_sdk_dlm.types.error_message
    import aws_sdk_dlm.types.parameter_list


class InvalidRequestException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_dlm.types.error_message.ErrorMessage"]
    code: NotRequired["aws_sdk_dlm.types.error_code.ErrorCode"]
    required_parameters: NotRequired["aws_sdk_dlm.types.parameter_list.ParameterList"]
    """<p>The request omitted one or more required parameters.</p>"""
    mutually_exclusive_parameters: NotRequired[
        "aws_sdk_dlm.types.parameter_list.ParameterList"
    ]
    """<p>The request included parameters that cannot be provided together.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "code" in value:
        out["Code"] = value["code"]
    if "required_parameters" in value:
        import aws_sdk_dlm.types.parameter_list

        out["RequiredParameters"] = aws_sdk_dlm.types.parameter_list.serialize_json(
            value["required_parameters"]
        )
    if "mutually_exclusive_parameters" in value:
        import aws_sdk_dlm.types.parameter_list

        out["MutuallyExclusiveParameters"] = (
            aws_sdk_dlm.types.parameter_list.serialize_json(
                value["mutually_exclusive_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> InvalidRequestException_:
    out: InvalidRequestException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Code" in data:
        out["code"] = data["Code"]
    if "RequiredParameters" in data:
        import aws_sdk_dlm.types.parameter_list

        out["required_parameters"] = aws_sdk_dlm.types.parameter_list.deserialize_json(
            data["RequiredParameters"]
        )
    if "MutuallyExclusiveParameters" in data:
        import aws_sdk_dlm.types.parameter_list

        out["mutually_exclusive_parameters"] = (
            aws_sdk_dlm.types.parameter_list.deserialize_json(
                data["MutuallyExclusiveParameters"]
            )
        )
    return out


class InvalidRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dlm#InvalidRequestException``."""

    code: str | None = "InvalidRequestException"

    def __init__(self, data: InvalidRequestException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRequestException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidRequestException":
        return cls(deserialize_json(data))
