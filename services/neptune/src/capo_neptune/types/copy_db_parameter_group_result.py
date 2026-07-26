"""Generated from Smithy shape ``com.amazonaws.neptune#CopyDBParameterGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.db_parameter_group


class CopyDBParameterGroupResult(TypedDict, closed=True):
    db_parameter_group: NotRequired[
        "capo_neptune.types.db_parameter_group.DBParameterGroup"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: CopyDBParameterGroupResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_parameter_group" in value:
        import capo_neptune.types.db_parameter_group

        capo_neptune.types.db_parameter_group.serialize_query(
            value["db_parameter_group"], pairs, f"{prefix}.DBParameterGroup"
        )


def deserialize_query(el: Element) -> CopyDBParameterGroupResult:
    out: CopyDBParameterGroupResult = {}  # type: ignore[typeddict-item]
    child_db_parameter_group = el.find("DBParameterGroup")
    if child_db_parameter_group is not None:
        import capo_neptune.types.db_parameter_group

        out["db_parameter_group"] = (
            capo_neptune.types.db_parameter_group.deserialize_query(
                child_db_parameter_group
            )
        )
    return out
