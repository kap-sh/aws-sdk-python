"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateApplicationStatusCheckResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.successful_association_response_set
    import capo_ec2.types.unsuccessful_association_response_set


class AssociateApplicationStatusCheckResult(TypedDict, closed=True):
    successful_results: NotRequired[
        "capo_ec2.types.successful_association_response_set.SuccessfulAssociationResponseSet"
    ]
    """<p>The associations that were successfully created.</p>"""
    unsuccessful_results: NotRequired[
        "capo_ec2.types.unsuccessful_association_response_set.UnsuccessfulAssociationResponseSet"
    ]
    """<p>The associations that failed to be created.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateApplicationStatusCheckResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "successful_results" in value:
        import capo_ec2.types.successful_association_response_set

        capo_ec2.types.successful_association_response_set.serialize_ec2_query(
            value["successful_results"], pairs, f"{key_prefix}SuccessfulResultSet"
        )
    if "unsuccessful_results" in value:
        import capo_ec2.types.unsuccessful_association_response_set

        capo_ec2.types.unsuccessful_association_response_set.serialize_ec2_query(
            value["unsuccessful_results"], pairs, f"{key_prefix}UnsuccessfulResultSet"
        )


def deserialize_ec2_query(el: Element) -> AssociateApplicationStatusCheckResult:
    out: AssociateApplicationStatusCheckResult = {}  # type: ignore[typeddict-item]
    child_successful_results = el.find("successfulResultSet")
    if child_successful_results is not None:
        import capo_ec2.types.successful_association_response_set

        out["successful_results"] = (
            capo_ec2.types.successful_association_response_set.deserialize_ec2_query(
                child_successful_results
            )
        )
    child_unsuccessful_results = el.find("unsuccessfulResultSet")
    if child_unsuccessful_results is not None:
        import capo_ec2.types.unsuccessful_association_response_set

        out["unsuccessful_results"] = (
            capo_ec2.types.unsuccessful_association_response_set.deserialize_ec2_query(
                child_unsuccessful_results
            )
        )
    return out
