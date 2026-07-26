"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#HitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudsearch_domain.types.hit

HitList: TypeAlias = list["capo_cloudsearch_domain.types.hit.Hit"]


# --- restJson1 ser/de ---
def serialize_json(value: HitList) -> list:
    import capo_cloudsearch_domain.types.hit

    out: list = []
    for item in value:
        out.append(capo_cloudsearch_domain.types.hit.serialize_json(item))
    return out


def deserialize_json(data: list) -> HitList:
    import capo_cloudsearch_domain.types.hit

    out: HitList = []
    for item in data:
        out.append(capo_cloudsearch_domain.types.hit.deserialize_json(item))
    return out
