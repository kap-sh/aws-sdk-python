"""Generated from Smithy shape ``com.amazonaws.ec2#ThroughResourcesStatementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.resource_statement_request


class ThroughResourcesStatementRequest(TypedDict, closed=True):
    resource_statement: NotRequired[
        "capo_ec2.types.resource_statement_request.ResourceStatementRequest"
    ]
    """<p>The resource statement.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ThroughResourcesStatementRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_statement" in value:
        import capo_ec2.types.resource_statement_request

        capo_ec2.types.resource_statement_request.serialize_ec2_query(
            value["resource_statement"], pairs, f"{prefix}.ResourceStatement"
        )


def deserialize_ec2_query(el: Element) -> ThroughResourcesStatementRequest:
    out: ThroughResourcesStatementRequest = {}  # type: ignore[typeddict-item]
    child_resource_statement = el.find("ResourceStatement")
    if child_resource_statement is not None:
        import capo_ec2.types.resource_statement_request

        out["resource_statement"] = (
            capo_ec2.types.resource_statement_request.deserialize_ec2_query(
                child_resource_statement
            )
        )
    return out
