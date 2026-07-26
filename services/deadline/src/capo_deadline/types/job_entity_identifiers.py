"""Generated from Smithy shape ``com.amazonaws.deadline#JobEntityIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.job_entity_identifiers_union

JobEntityIdentifiers: TypeAlias = list[
    "capo_deadline.types.job_entity_identifiers_union.JobEntityIdentifiersUnion"
]


# --- restJson1 ser/de ---
def serialize_json(value: JobEntityIdentifiers) -> list:
    import capo_deadline.types.job_entity_identifiers_union

    out: list = []
    for item in value:
        out.append(
            capo_deadline.types.job_entity_identifiers_union.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> JobEntityIdentifiers:
    import capo_deadline.types.job_entity_identifiers_union

    out: JobEntityIdentifiers = []
    for item in data:
        out.append(
            capo_deadline.types.job_entity_identifiers_union.deserialize_json(item)
        )
    return out
