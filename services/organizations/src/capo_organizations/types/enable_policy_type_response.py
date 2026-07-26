"""Generated from Smithy shape ``com.amazonaws.organizations#EnablePolicyTypeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.root


class EnablePolicyTypeResponse(TypedDict, closed=True):
    root: NotRequired["capo_organizations.types.root.Root"]
    """<p>A structure that shows the root with the updated list of enabled policy types.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnablePolicyTypeResponse) -> dict:
    out: dict = {}
    if "root" in value:
        import capo_organizations.types.root

        out["Root"] = capo_organizations.types.root.serialize_aws_json_1_1(
            value["root"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnablePolicyTypeResponse:
    out: EnablePolicyTypeResponse = {}  # type: ignore[typeddict-item]
    if "Root" in data:
        import capo_organizations.types.root

        out["root"] = capo_organizations.types.root.deserialize_aws_json_1_1(
            data["Root"]
        )
    return out
