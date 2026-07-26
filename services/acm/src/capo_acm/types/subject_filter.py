"""Generated from Smithy shape ``com.amazonaws.acm#SubjectFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_acm.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_acm.types.common_name_filter


class _SubjectFilter_CommonName(TypedDict, closed=True):
    CommonName: "capo_acm.types.common_name_filter.CommonNameFilter"


SubjectFilter: TypeAlias = _SubjectFilter_CommonName


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubjectFilter) -> dict:
    if "CommonName" in value:
        import capo_acm.types.common_name_filter

        return {
            "CommonName": capo_acm.types.common_name_filter.serialize_aws_json_1_1(
                value["CommonName"]
            )
        }
    else:
        raise SerializationError("SubjectFilter: no variant present")


def deserialize_aws_json_1_1(data: dict) -> SubjectFilter:
    if "CommonName" in data:
        import capo_acm.types.common_name_filter

        return {
            "CommonName": capo_acm.types.common_name_filter.deserialize_aws_json_1_1(
                data["CommonName"]
            )
        }
    else:
        raise DeserializationError("SubjectFilter: no recognized variant key")
