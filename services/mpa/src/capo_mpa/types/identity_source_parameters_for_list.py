"""Generated from Smithy shape ``com.amazonaws.mpa#IdentitySourceParametersForList``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mpa.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_mpa.types.iam_identity_center_for_list


class _IdentitySourceParametersForList_IamIdentityCenter(TypedDict, closed=True):
    IamIdentityCenter: (
        "capo_mpa.types.iam_identity_center_for_list.IamIdentityCenterForList"
    )


IdentitySourceParametersForList: TypeAlias = (
    _IdentitySourceParametersForList_IamIdentityCenter
)


# --- restJson1 ser/de ---
def serialize_json(value: IdentitySourceParametersForList) -> dict:
    if "IamIdentityCenter" in value:
        import capo_mpa.types.iam_identity_center_for_list

        return {
            "IamIdentityCenter": capo_mpa.types.iam_identity_center_for_list.serialize_json(
                value["IamIdentityCenter"]
            )
        }
    else:
        raise SerializationError("IdentitySourceParametersForList: no variant present")


def deserialize_json(data: dict) -> IdentitySourceParametersForList:
    if "IamIdentityCenter" in data:
        import capo_mpa.types.iam_identity_center_for_list

        return {
            "IamIdentityCenter": capo_mpa.types.iam_identity_center_for_list.deserialize_json(
                data["IamIdentityCenter"]
            )
        }
    else:
        raise DeserializationError(
            "IdentitySourceParametersForList: no recognized variant key"
        )
