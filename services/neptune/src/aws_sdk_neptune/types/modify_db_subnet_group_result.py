"""Generated from Smithy shape ``com.amazonaws.neptune#ModifyDBSubnetGroupResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.db_subnet_group


class ModifyDBSubnetGroupResult(TypedDict):
    db_subnet_group: NotRequired["aws_sdk_neptune.types.db_subnet_group.DBSubnetGroup"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBSubnetGroupResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_subnet_group" in value:
        import aws_sdk_neptune.types.db_subnet_group

        aws_sdk_neptune.types.db_subnet_group.serialize_query(
            value["db_subnet_group"], pairs, f"{prefix}.DBSubnetGroup"
        )


def deserialize_query(el: Element) -> ModifyDBSubnetGroupResult:
    out: ModifyDBSubnetGroupResult = {}  # type: ignore[typeddict-item]
    child_db_subnet_group = el.find("DBSubnetGroup")
    if child_db_subnet_group is not None:
        import aws_sdk_neptune.types.db_subnet_group

        out["db_subnet_group"] = (
            aws_sdk_neptune.types.db_subnet_group.deserialize_query(
                child_db_subnet_group
            )
        )
    return out
