"""Generated from Smithy shape ``com.amazonaws.acm#ListCertificatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_acm.types.certificate_statuses
    import aws_sdk_acm.types.filters
    import aws_sdk_acm.types.max_items
    import aws_sdk_acm.types.next_token
    import aws_sdk_acm.types.sort_by
    import aws_sdk_acm.types.sort_order


class ListCertificatesRequest(TypedDict, closed=True):
    certificate_statuses: NotRequired[
        "aws_sdk_acm.types.certificate_statuses.CertificateStatuses"
    ]
    """<p>Filter the certificate list by status value.</p>"""
    includes: NotRequired["aws_sdk_acm.types.filters.Filters"]
    """<p>Filter the certificate list. For more information, see the <a>Filters</a> structure.</p>"""
    next_token: NotRequired["aws_sdk_acm.types.next_token.NextToken"]
    """<p>Use this parameter only when paginating results and only in a subsequent request after you receive a response with truncated results. Set it to the value of <code>NextToken</code> from the response you just received.</p>"""
    max_items: NotRequired["aws_sdk_acm.types.max_items.MaxItems"]
    """<p>Use this parameter when paginating results to specify the maximum number of items to return in the response. If additional items exist beyond the number you specify, the <code>NextToken</code> element is sent in the response. Use this <code>NextToken</code> value in a subsequent request to retrieve additional items.</p>"""
    sort_by: NotRequired["aws_sdk_acm.types.sort_by.SortBy"]
    """<p>Specifies the field to sort results by. If you specify <code>SortBy</code>, you must also specify <code>SortOrder</code>.</p>"""
    sort_order: NotRequired["aws_sdk_acm.types.sort_order.SortOrder"]
    """<p>Specifies the order of sorted results. If you specify <code>SortOrder</code>, you must also specify <code>SortBy</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCertificatesRequest) -> dict:
    out: dict = {}
    if "certificate_statuses" in value:
        import aws_sdk_acm.types.certificate_statuses

        out["CertificateStatuses"] = (
            aws_sdk_acm.types.certificate_statuses.serialize_aws_json_1_1(
                value["certificate_statuses"]
            )
        )
    if "includes" in value:
        import aws_sdk_acm.types.filters

        out["Includes"] = aws_sdk_acm.types.filters.serialize_aws_json_1_1(
            value["includes"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_items" in value:
        out["MaxItems"] = value["max_items"]
    if "sort_by" in value:
        import aws_sdk_acm.types.sort_by

        out["SortBy"] = aws_sdk_acm.types.sort_by.serialize_aws_json_1_1(
            value["sort_by"]
        )
    if "sort_order" in value:
        import aws_sdk_acm.types.sort_order

        out["SortOrder"] = aws_sdk_acm.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCertificatesRequest:
    out: ListCertificatesRequest = {}  # type: ignore[typeddict-item]
    if "CertificateStatuses" in data:
        import aws_sdk_acm.types.certificate_statuses

        out["certificate_statuses"] = (
            aws_sdk_acm.types.certificate_statuses.deserialize_aws_json_1_1(
                data["CertificateStatuses"]
            )
        )
    if "Includes" in data:
        import aws_sdk_acm.types.filters

        out["includes"] = aws_sdk_acm.types.filters.deserialize_aws_json_1_1(
            data["Includes"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxItems" in data:
        out["max_items"] = data["MaxItems"]
    if "SortBy" in data:
        import aws_sdk_acm.types.sort_by

        out["sort_by"] = aws_sdk_acm.types.sort_by.deserialize_aws_json_1_1(
            data["SortBy"]
        )
    if "SortOrder" in data:
        import aws_sdk_acm.types.sort_order

        out["sort_order"] = aws_sdk_acm.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    return out
