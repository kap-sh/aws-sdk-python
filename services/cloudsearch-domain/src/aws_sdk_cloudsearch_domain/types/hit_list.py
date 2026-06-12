"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#HitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudsearch_domain.types.hit

HitList: TypeAlias = list["aws_sdk_cloudsearch_domain.types.hit.Hit"]


# --- restJson1 ser/de ---
def serialize_json(value: HitList) -> list:
    import aws_sdk_cloudsearch_domain.types.hit

    out: list = []
    for item in value:
        out.append(aws_sdk_cloudsearch_domain.types.hit.serialize_json(item))
    return out


def deserialize_json(data: list) -> HitList:
    import aws_sdk_cloudsearch_domain.types.hit

    out: HitList = []
    for item in data:
        out.append(aws_sdk_cloudsearch_domain.types.hit.deserialize_json(item))
    return out
