"""Generated from Smithy shape ``com.amazonaws.lightsail#GetCertificatesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.certificate_summary_list
    import aws_sdk_lightsail.types.string


class GetCertificatesResult(TypedDict):
    certificates: NotRequired[
        "aws_sdk_lightsail.types.certificate_summary_list.CertificateSummaryList"
    ]
    """<p>An object that describes certificates.</p>"""
    next_page_token: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>If <code>NextPageToken</code> is returned there are more results available. The value of <code>NextPageToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCertificatesResult) -> dict:
    out: dict = {}
    if "certificates" in value:
        import aws_sdk_lightsail.types.certificate_summary_list

        out["certificates"] = (
            aws_sdk_lightsail.types.certificate_summary_list.serialize_aws_json_1_1(
                value["certificates"]
            )
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCertificatesResult:
    out: GetCertificatesResult = {}  # type: ignore[typeddict-item]
    if "certificates" in data:
        import aws_sdk_lightsail.types.certificate_summary_list

        out["certificates"] = (
            aws_sdk_lightsail.types.certificate_summary_list.deserialize_aws_json_1_1(
                data["certificates"]
            )
        )
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out
