"""Generated from Smithy shape ``com.amazonaws.wafv2#GetMobileSdkReleaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.platform
    import aws_sdk_wafv2.types.version_key_string


class GetMobileSdkReleaseRequest(TypedDict, closed=True):
    platform: "aws_sdk_wafv2.types.platform.Platform"
    """<p>The device platform.</p>"""
    release_version: "aws_sdk_wafv2.types.version_key_string.VersionKeyString"
    """<p>The release version. For the latest available version, specify <code>LATEST</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMobileSdkReleaseRequest) -> dict:
    out: dict = {}
    import aws_sdk_wafv2.types.platform

    out["Platform"] = aws_sdk_wafv2.types.platform.serialize_aws_json_1_1(
        value["platform"]
    )
    out["ReleaseVersion"] = value["release_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMobileSdkReleaseRequest:
    out: GetMobileSdkReleaseRequest = {}  # type: ignore[typeddict-item]
    if "Platform" in data:
        import aws_sdk_wafv2.types.platform

        out["platform"] = aws_sdk_wafv2.types.platform.deserialize_aws_json_1_1(
            data["Platform"]
        )
    else:
        raise DeserializationError("GetMobileSdkReleaseRequest.platform required")
    if "ReleaseVersion" in data:
        out["release_version"] = data["ReleaseVersion"]
    else:
        raise DeserializationError(
            "GetMobileSdkReleaseRequest.release_version required"
        )
    return out
