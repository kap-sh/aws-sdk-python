"""Generated from Smithy shape ``com.amazonaws.mpa#IdentitySourceParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.iam_identity_center


class IdentitySourceParameters(TypedDict, closed=True):
    iam_identity_center: NotRequired[
        "capo_mpa.types.iam_identity_center.IamIdentityCenter"
    ]
    """<p>IAM Identity Center credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdentitySourceParameters) -> dict:
    out: dict = {}
    if "iam_identity_center" in value:
        import capo_mpa.types.iam_identity_center

        out["IamIdentityCenter"] = capo_mpa.types.iam_identity_center.serialize_json(
            value["iam_identity_center"]
        )
    return out


def deserialize_json(data: dict) -> IdentitySourceParameters:
    out: IdentitySourceParameters = {}  # type: ignore[typeddict-item]
    if "IamIdentityCenter" in data:
        import capo_mpa.types.iam_identity_center

        out["iam_identity_center"] = (
            capo_mpa.types.iam_identity_center.deserialize_json(
                data["IamIdentityCenter"]
            )
        )
    return out
