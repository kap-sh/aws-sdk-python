"""Generated from Smithy shape ``com.amazonaws.servicediscovery#DnsConfigChange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.dns_record_list


class DnsConfigChange(TypedDict, closed=True):
    dns_records: "aws_sdk_servicediscovery.types.dns_record_list.DnsRecordList"
    """<p>An array that contains one <code>DnsRecord</code> object for each Route 53 record that you want Cloud Map to create when you register an instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsConfigChange) -> dict:
    out: dict = {}
    import aws_sdk_servicediscovery.types.dns_record_list

    out["DnsRecords"] = (
        aws_sdk_servicediscovery.types.dns_record_list.serialize_aws_json_1_1(
            value["dns_records"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DnsConfigChange:
    out: DnsConfigChange = {}  # type: ignore[typeddict-item]
    if "DnsRecords" in data:
        import aws_sdk_servicediscovery.types.dns_record_list

        out["dns_records"] = (
            aws_sdk_servicediscovery.types.dns_record_list.deserialize_aws_json_1_1(
                data["DnsRecords"]
            )
        )
    else:
        raise DeserializationError("DnsConfigChange.dns_records required")
    return out
