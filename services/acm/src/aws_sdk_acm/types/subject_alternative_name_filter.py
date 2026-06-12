"""Generated from Smithy shape ``com.amazonaws.acm#SubjectAlternativeNameFilter``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_acm.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_acm.types.dns_name_filter


class _SubjectAlternativeNameFilter_DnsName(TypedDict):
    DnsName: "aws_sdk_acm.types.dns_name_filter.DnsNameFilter"


SubjectAlternativeNameFilter: TypeAlias = _SubjectAlternativeNameFilter_DnsName


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubjectAlternativeNameFilter) -> dict:
    if "DnsName" in value:
        import aws_sdk_acm.types.dns_name_filter

        return {
            "DnsName": aws_sdk_acm.types.dns_name_filter.serialize_aws_json_1_1(
                value["DnsName"]
            )
        }
    else:
        raise SerializationError("SubjectAlternativeNameFilter: no variant present")


def deserialize_aws_json_1_1(data: dict) -> SubjectAlternativeNameFilter:
    if "DnsName" in data:
        import aws_sdk_acm.types.dns_name_filter

        return {
            "DnsName": aws_sdk_acm.types.dns_name_filter.deserialize_aws_json_1_1(
                data["DnsName"]
            )
        }
    else:
        raise DeserializationError(
            "SubjectAlternativeNameFilter: no recognized variant key"
        )
