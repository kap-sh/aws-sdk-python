"""Generated from Smithy shape ``com.amazonaws.neptune#CreateDBParameterGroupResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.db_parameter_group


class CreateDBParameterGroupResult(TypedDict):
    db_parameter_group: NotRequired[
        "aws_sdk_neptune.types.db_parameter_group.DBParameterGroup"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateDBParameterGroupResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_parameter_group" in value:
        import aws_sdk_neptune.types.db_parameter_group

        aws_sdk_neptune.types.db_parameter_group.serialize_query(
            value["db_parameter_group"], pairs, f"{prefix}.DBParameterGroup"
        )


def deserialize_query(el: Element) -> CreateDBParameterGroupResult:
    out: CreateDBParameterGroupResult = {}  # type: ignore[typeddict-item]
    child_db_parameter_group = el.find("DBParameterGroup")
    if child_db_parameter_group is not None:
        import aws_sdk_neptune.types.db_parameter_group

        out["db_parameter_group"] = (
            aws_sdk_neptune.types.db_parameter_group.deserialize_query(
                child_db_parameter_group
            )
        )
    return out
