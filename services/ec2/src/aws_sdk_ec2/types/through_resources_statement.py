"""Generated from Smithy shape ``com.amazonaws.ec2#ThroughResourcesStatement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.resource_statement


class ThroughResourcesStatement(TypedDict):
    resource_statement: NotRequired[
        "aws_sdk_ec2.types.resource_statement.ResourceStatement"
    ]
    """<p>The resource statement.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ThroughResourcesStatement, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_statement" in value:
        import aws_sdk_ec2.types.resource_statement

        aws_sdk_ec2.types.resource_statement.serialize_ec2_query(
            value["resource_statement"], pairs, f"{prefix}.ResourceStatement"
        )


def deserialize_ec2_query(el: Element) -> ThroughResourcesStatement:
    out: ThroughResourcesStatement = {}  # type: ignore[typeddict-item]
    child_resource_statement = el.find("ResourceStatement")
    if child_resource_statement is not None:
        import aws_sdk_ec2.types.resource_statement

        out["resource_statement"] = (
            aws_sdk_ec2.types.resource_statement.deserialize_ec2_query(
                child_resource_statement
            )
        )
    return out
