"""Generated from Smithy shape ``com.amazonaws.ses#MessageDsn``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.arrival_date
    import aws_sdk_ses.types.extension_field_list
    import aws_sdk_ses.types.reporting_mta


class MessageDsn(TypedDict, closed=True):
    reporting_mta: "aws_sdk_ses.types.reporting_mta.ReportingMta"
    r"""<p>The reporting MTA that attempted to deliver the message, formatted as specified in <a href=\"https://tools.ietf.org/html/rfc3464\">RFC 3464</a> (<code>mta-name-type; mta-name</code>). The default value is <code>dns; inbound-smtp.[region].amazonaws.com</code>.</p>"""
    arrival_date: NotRequired["aws_sdk_ses.types.arrival_date.ArrivalDate"]
    r"""<p>When the message was received by the reporting mail transfer agent (MTA), in <a href=\"https://www.ietf.org/rfc/rfc0822.txt\">RFC 822</a> date-time format.</p>"""
    extension_fields: NotRequired[
        "aws_sdk_ses.types.extension_field_list.ExtensionFieldList"
    ]
    """<p>Additional X-headers to include in the DSN.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: MessageDsn, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.ReportingMta", str(value["reporting_mta"])))
    if "arrival_date" in value:
        import aws_sdk_ses.types.arrival_date

        aws_sdk_ses.types.arrival_date.serialize_query(
            value["arrival_date"], pairs, f"{prefix}.ArrivalDate"
        )
    if "extension_fields" in value:
        import aws_sdk_ses.types.extension_field_list

        aws_sdk_ses.types.extension_field_list.serialize_query(
            value["extension_fields"], pairs, f"{prefix}.ExtensionFields"
        )


def deserialize_query(el: Element) -> MessageDsn:
    out: MessageDsn = {}  # type: ignore[typeddict-item]
    child_reporting_mta = el.find("ReportingMta")
    if child_reporting_mta is not None:
        out["reporting_mta"] = str(child_reporting_mta.text or "")
    else:
        raise DeserializationError("MessageDsn.reporting_mta required")
    child_arrival_date = el.find("ArrivalDate")
    if child_arrival_date is not None:
        import aws_sdk_ses.types.arrival_date

        out["arrival_date"] = aws_sdk_ses.types.arrival_date.deserialize_query(
            child_arrival_date
        )
    child_extension_fields = el.find("ExtensionFields")
    if child_extension_fields is not None:
        import aws_sdk_ses.types.extension_field_list

        out["extension_fields"] = (
            aws_sdk_ses.types.extension_field_list.deserialize_query(
                child_extension_fields
            )
        )
    return out
