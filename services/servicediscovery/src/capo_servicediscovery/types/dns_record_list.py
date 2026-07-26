"""Generated from Smithy shape ``com.amazonaws.servicediscovery#DnsRecordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_servicediscovery.types.dns_record

DnsRecordList: TypeAlias = list["capo_servicediscovery.types.dns_record.DnsRecord"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsRecordList) -> list:
    import capo_servicediscovery.types.dns_record

    out: list = []
    for item in value:
        out.append(capo_servicediscovery.types.dns_record.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DnsRecordList:
    import capo_servicediscovery.types.dns_record

    out: DnsRecordList = []
    for item in data:
        out.append(
            capo_servicediscovery.types.dns_record.deserialize_aws_json_1_1(item)
        )
    return out
