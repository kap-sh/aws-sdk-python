"""Generated from Smithy shape ``com.amazonaws.ec2#CreateApplicationStatusCheckResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.application_status_check_response_object


class CreateApplicationStatusCheckResult(TypedDict, closed=True):
    application_status_check: NotRequired[
        "capo_ec2.types.application_status_check_response_object.ApplicationStatusCheckResponseObject"
    ]
    """<p>Information about the application status check.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateApplicationStatusCheckResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "application_status_check" in value:
        import capo_ec2.types.application_status_check_response_object

        capo_ec2.types.application_status_check_response_object.serialize_ec2_query(
            value["application_status_check"],
            pairs,
            f"{key_prefix}ApplicationStatusCheck",
        )


def deserialize_ec2_query(el: Element) -> CreateApplicationStatusCheckResult:
    out: CreateApplicationStatusCheckResult = {}  # type: ignore[typeddict-item]
    child_application_status_check = el.find("applicationStatusCheck")
    if child_application_status_check is not None:
        import capo_ec2.types.application_status_check_response_object

        out["application_status_check"] = (
            capo_ec2.types.application_status_check_response_object.deserialize_ec2_query(
                child_application_status_check
            )
        )
    return out
