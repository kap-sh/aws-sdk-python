"""Generated from Smithy shape ``com.amazonaws.docdb#DescribeCertificatesMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.filter_list
    import aws_sdk_docdb.types.integer_optional
    import aws_sdk_docdb.types.string


class DescribeCertificatesMessage(TypedDict, closed=True):
    certificate_identifier: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The user-supplied certificate identifier. If this parameter is specified, information for only the specified certificate is returned. If this parameter is omitted, a list of up to <code>MaxRecords</code> certificates is returned. This parameter is not case sensitive.</p> <p>Constraints</p> <ul> <li> <p>Must match an existing <code>CertificateIdentifier</code>.</p> </li> </ul>"""
    filters: NotRequired["aws_sdk_docdb.types.filter_list.FilterList"]
    """<p>This parameter is not currently supported.</p>"""
    max_records: NotRequired["aws_sdk_docdb.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints:</p> <ul> <li> <p>Minimum: 20</p> </li> <li> <p>Maximum: 100</p> </li> </ul>"""
    marker: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeCertificates</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeCertificatesMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "certificate_identifier" in value:
        pairs.append(
            (f"{prefix}.CertificateIdentifier", str(value["certificate_identifier"]))
        )
    if "filters" in value:
        import aws_sdk_docdb.types.filter_list

        aws_sdk_docdb.types.filter_list.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeCertificatesMessage:
    out: DescribeCertificatesMessage = {}  # type: ignore[typeddict-item]
    child_certificate_identifier = el.find("CertificateIdentifier")
    if child_certificate_identifier is not None:
        out["certificate_identifier"] = str(child_certificate_identifier.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import aws_sdk_docdb.types.filter_list

        out["filters"] = aws_sdk_docdb.types.filter_list.deserialize_query(
            child_filters
        )
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
