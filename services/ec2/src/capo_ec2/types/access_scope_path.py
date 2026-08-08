"""Generated from Smithy shape ``com.amazonaws.ec2#AccessScopePath``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.path_statement
    import capo_ec2.types.through_resources_statement_list


class AccessScopePath(TypedDict, closed=True):
    source: NotRequired["capo_ec2.types.path_statement.PathStatement"]
    """<p>The source.</p>"""
    destination: NotRequired["capo_ec2.types.path_statement.PathStatement"]
    """<p>The destination.</p>"""
    through_resources: NotRequired[
        "capo_ec2.types.through_resources_statement_list.ThroughResourcesStatementList"
    ]
    """<p>The through resources.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AccessScopePath, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source" in value:
        import capo_ec2.types.path_statement

        capo_ec2.types.path_statement.serialize_ec2_query(
            value["source"], pairs, f"{key_prefix}Source"
        )
    if "destination" in value:
        import capo_ec2.types.path_statement

        capo_ec2.types.path_statement.serialize_ec2_query(
            value["destination"], pairs, f"{key_prefix}Destination"
        )
    if "through_resources" in value:
        import capo_ec2.types.through_resources_statement_list

        capo_ec2.types.through_resources_statement_list.serialize_ec2_query(
            value["through_resources"], pairs, f"{key_prefix}ThroughResourceSet"
        )


def deserialize_ec2_query(el: Element) -> AccessScopePath:
    out: AccessScopePath = {}  # type: ignore[typeddict-item]
    child_source = el.find("source")
    if child_source is not None:
        import capo_ec2.types.path_statement

        out["source"] = capo_ec2.types.path_statement.deserialize_ec2_query(
            child_source
        )
    child_destination = el.find("destination")
    if child_destination is not None:
        import capo_ec2.types.path_statement

        out["destination"] = capo_ec2.types.path_statement.deserialize_ec2_query(
            child_destination
        )
    if el.find("throughResourceSet") is not None:
        import capo_ec2.types.through_resources_statement_list

        out["through_resources"] = (
            capo_ec2.types.through_resources_statement_list.deserialize_ec2_query(
                el, "throughResourceSet"
            )
        )
    return out
