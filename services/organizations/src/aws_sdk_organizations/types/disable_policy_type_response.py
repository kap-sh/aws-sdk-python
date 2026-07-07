"""Generated from Smithy shape ``com.amazonaws.organizations#DisablePolicyTypeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_organizations.types.root


class DisablePolicyTypeResponse(TypedDict, closed=True):
    root: NotRequired["aws_sdk_organizations.types.root.Root"]
    """<p>A structure that shows the root with the updated list of enabled policy types.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisablePolicyTypeResponse) -> dict:
    out: dict = {}
    if "root" in value:
        import aws_sdk_organizations.types.root

        out["Root"] = aws_sdk_organizations.types.root.serialize_aws_json_1_1(
            value["root"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DisablePolicyTypeResponse:
    out: DisablePolicyTypeResponse = {}  # type: ignore[typeddict-item]
    if "Root" in data:
        import aws_sdk_organizations.types.root

        out["root"] = aws_sdk_organizations.types.root.deserialize_aws_json_1_1(
            data["Root"]
        )
    return out
