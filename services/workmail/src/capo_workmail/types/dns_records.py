"""Generated from Smithy shape ``com.amazonaws.workmail#DnsRecords``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workmail.types.dns_record

DnsRecords: TypeAlias = list["capo_workmail.types.dns_record.DnsRecord"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsRecords) -> list:
    import capo_workmail.types.dns_record

    out: list = []
    for item in value:
        out.append(capo_workmail.types.dns_record.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DnsRecords:
    import capo_workmail.types.dns_record

    out: DnsRecords = []
    for item in data:
        out.append(capo_workmail.types.dns_record.deserialize_aws_json_1_1(item))
    return out
