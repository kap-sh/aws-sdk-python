"""Generated from Smithy shape ``com.amazonaws.appstream#Filters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.filter

Filters: TypeAlias = list["capo_appstream.types.filter.Filter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filters) -> list:
    import capo_appstream.types.filter

    out: list = []
    for item in value:
        out.append(capo_appstream.types.filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Filters:
    import capo_appstream.types.filter

    out: Filters = []
    for item in data:
        out.append(capo_appstream.types.filter.deserialize_aws_json_1_1(item))
    return out
