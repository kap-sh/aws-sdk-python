"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ListTrustStoreCertificatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn
    import aws_sdk_workspaces_web.types.certificate_summary_list
    import aws_sdk_workspaces_web.types.pagination_token


class ListTrustStoreCertificatesResponse(TypedDict, closed=True):
    certificate_list: NotRequired[
        "aws_sdk_workspaces_web.types.certificate_summary_list.CertificateSummaryList"
    ]
    """<p>The certificate list.</p>"""
    trust_store_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the trust store.</p>"""
    next_token: NotRequired[
        "aws_sdk_workspaces_web.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token used to retrieve the next page of results for this operation.&gt;</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTrustStoreCertificatesResponse) -> dict:
    out: dict = {}
    if "certificate_list" in value:
        import aws_sdk_workspaces_web.types.certificate_summary_list

        out["certificateList"] = (
            aws_sdk_workspaces_web.types.certificate_summary_list.serialize_json(
                value["certificate_list"]
            )
        )
    out["trustStoreArn"] = value["trust_store_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTrustStoreCertificatesResponse:
    out: ListTrustStoreCertificatesResponse = {}  # type: ignore[typeddict-item]
    if "certificateList" in data:
        import aws_sdk_workspaces_web.types.certificate_summary_list

        out["certificate_list"] = (
            aws_sdk_workspaces_web.types.certificate_summary_list.deserialize_json(
                data["certificateList"]
            )
        )
    if "trustStoreArn" in data:
        out["trust_store_arn"] = data["trustStoreArn"]
    else:
        raise DeserializationError(
            "ListTrustStoreCertificatesResponse.trust_store_arn required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
