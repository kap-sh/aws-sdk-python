"""Generated from Smithy shape ``com.amazonaws.ec2#AccessScopePath``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.path_statement
    import aws_sdk_ec2.types.through_resources_statement_list


class AccessScopePath(TypedDict):
    source: NotRequired["aws_sdk_ec2.types.path_statement.PathStatement"]
    """<p>The source.</p>"""
    destination: NotRequired["aws_sdk_ec2.types.path_statement.PathStatement"]
    """<p>The destination.</p>"""
    through_resources: NotRequired[
        "aws_sdk_ec2.types.through_resources_statement_list.ThroughResourcesStatementList"
    ]
    """<p>The through resources.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AccessScopePath, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "source" in value:
        import aws_sdk_ec2.types.path_statement

        aws_sdk_ec2.types.path_statement.serialize_ec2_query(
            value["source"], pairs, f"{prefix}.Source"
        )
    if "destination" in value:
        import aws_sdk_ec2.types.path_statement

        aws_sdk_ec2.types.path_statement.serialize_ec2_query(
            value["destination"], pairs, f"{prefix}.Destination"
        )
    if "through_resources" in value:
        import aws_sdk_ec2.types.through_resources_statement_list

        aws_sdk_ec2.types.through_resources_statement_list.serialize_ec2_query(
            value["through_resources"], pairs, f"{prefix}.ThroughResourceSet"
        )


def deserialize_ec2_query(el: Element) -> AccessScopePath:
    out: AccessScopePath = {}  # type: ignore[typeddict-item]
    child_source = el.find("Source")
    if child_source is not None:
        import aws_sdk_ec2.types.path_statement

        out["source"] = aws_sdk_ec2.types.path_statement.deserialize_ec2_query(
            child_source
        )
    child_destination = el.find("Destination")
    if child_destination is not None:
        import aws_sdk_ec2.types.path_statement

        out["destination"] = aws_sdk_ec2.types.path_statement.deserialize_ec2_query(
            child_destination
        )
    if el.find("ThroughResourceSet") is not None:
        import aws_sdk_ec2.types.through_resources_statement_list

        out["through_resources"] = (
            aws_sdk_ec2.types.through_resources_statement_list.deserialize_ec2_query(
                el, "ThroughResourceSet"
            )
        )
    return out
