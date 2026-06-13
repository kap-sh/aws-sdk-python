"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ListCertificateAssociationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.certificate_association_summary_list


class ListCertificateAssociationsResponse(TypedDict):
    certificate_associations: "aws_sdk_rtbfabric.types.certificate_association_summary_list.CertificateAssociationSummaryList"
    """<p>The list of certificate associations for the gateway.</p>"""
    next_token: NotRequired["str"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCertificateAssociationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_rtbfabric.types.certificate_association_summary_list

    out["certificateAssociations"] = (
        aws_sdk_rtbfabric.types.certificate_association_summary_list.serialize_json(
            value["certificate_associations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCertificateAssociationsResponse:
    out: ListCertificateAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "certificateAssociations" in data:
        import aws_sdk_rtbfabric.types.certificate_association_summary_list

        out["certificate_associations"] = (
            aws_sdk_rtbfabric.types.certificate_association_summary_list.deserialize_json(
                data["certificateAssociations"]
            )
        )
    else:
        raise DeserializationError(
            "ListCertificateAssociationsResponse.certificate_associations required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
