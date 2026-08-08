"""Generated from Smithy shape ``com.amazonaws.ec2#ValidationWarning``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.error_set


class ValidationWarning(TypedDict, closed=True):
    errors: NotRequired["capo_ec2.types.error_set.ErrorSet"]
    """<p>The error codes and error messages.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ValidationWarning, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "errors" in value:
        import capo_ec2.types.error_set

        capo_ec2.types.error_set.serialize_ec2_query(
            value["errors"], pairs, f"{key_prefix}ErrorSet"
        )


def deserialize_ec2_query(el: Element) -> ValidationWarning:
    out: ValidationWarning = {}  # type: ignore[typeddict-item]
    if el.find("errorSet") is not None:
        import capo_ec2.types.error_set

        out["errors"] = capo_ec2.types.error_set.deserialize_ec2_query(el, "errorSet")
    return out
