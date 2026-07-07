"""Generated from Smithy shape ``com.amazonaws.wafv2#GetMobileSdkReleaseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.mobile_sdk_release


class GetMobileSdkReleaseResponse(TypedDict, closed=True):
    mobile_sdk_release: NotRequired[
        "aws_sdk_wafv2.types.mobile_sdk_release.MobileSdkRelease"
    ]
    """<p>Information for a specified SDK release, including release notes and tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMobileSdkReleaseResponse) -> dict:
    out: dict = {}
    if "mobile_sdk_release" in value:
        import aws_sdk_wafv2.types.mobile_sdk_release

        out["MobileSdkRelease"] = (
            aws_sdk_wafv2.types.mobile_sdk_release.serialize_aws_json_1_1(
                value["mobile_sdk_release"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMobileSdkReleaseResponse:
    out: GetMobileSdkReleaseResponse = {}  # type: ignore[typeddict-item]
    if "MobileSdkRelease" in data:
        import aws_sdk_wafv2.types.mobile_sdk_release

        out["mobile_sdk_release"] = (
            aws_sdk_wafv2.types.mobile_sdk_release.deserialize_aws_json_1_1(
                data["MobileSdkRelease"]
            )
        )
    return out
