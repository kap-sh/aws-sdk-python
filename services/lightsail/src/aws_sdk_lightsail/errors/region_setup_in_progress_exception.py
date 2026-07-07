"""Generated from Smithy shape ``com.amazonaws.lightsail#RegionSetupInProgressException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lightsail.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.string


class RegionSetupInProgressException_(TypedDict, closed=True):
    code: NotRequired["aws_sdk_lightsail.types.string.string"]
    docs: NotRequired["aws_sdk_lightsail.types.string.string"]
    r"""<p> <a href=\"https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-regions-and-availability-zones-in-amazon-lightsail.html\">Regions and Availability Zones for Lightsail</a> </p>"""
    message: NotRequired["aws_sdk_lightsail.types.string.string"]
    tip: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>Opt-in Regions typically take a few minutes to finish setting up before you can work with them. Wait a few minutes and try again.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegionSetupInProgressException_) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "docs" in value:
        out["docs"] = value["docs"]
    if "message" in value:
        out["message"] = value["message"]
    if "tip" in value:
        out["tip"] = value["tip"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegionSetupInProgressException_:
    out: RegionSetupInProgressException_ = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    if "docs" in data:
        out["docs"] = data["docs"]
    if "message" in data:
        out["message"] = data["message"]
    if "tip" in data:
        out["tip"] = data["tip"]
    return out


class RegionSetupInProgressException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lightsail#RegionSetupInProgressException``."""

    code: str | None = "RegionSetupInProgressException"

    def __init__(self, data: RegionSetupInProgressException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RegionSetupInProgressException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "RegionSetupInProgressException":
        return cls(deserialize_aws_json_1_1(data))
