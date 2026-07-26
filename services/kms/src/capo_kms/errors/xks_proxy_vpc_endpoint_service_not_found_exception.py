"""Generated from Smithy shape ``com.amazonaws.kms#XksProxyVpcEndpointServiceNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kms.errors import ServiceError

if TYPE_CHECKING:
    import capo_kms.types.error_message_type


class XksProxyVpcEndpointServiceNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_kms.types.error_message_type.ErrorMessageType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: XksProxyVpcEndpointServiceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> XksProxyVpcEndpointServiceNotFoundException_:
    out: XksProxyVpcEndpointServiceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class XksProxyVpcEndpointServiceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#XksProxyVpcEndpointServiceNotFoundException``."""

    code: str | None = "XksProxyVpcEndpointServiceNotFoundException"

    def __init__(self, data: XksProxyVpcEndpointServiceNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="XksProxyVpcEndpointServiceNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "XksProxyVpcEndpointServiceNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
