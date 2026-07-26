"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeLifecycleConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.data_lake_lifecycle_expiration
    import capo_securitylake.types.data_lake_lifecycle_transition_list


class DataLakeLifecycleConfiguration(TypedDict, closed=True):
    expiration: NotRequired[
        "capo_securitylake.types.data_lake_lifecycle_expiration.DataLakeLifecycleExpiration"
    ]
    """<p>Provides data expiration details of Amazon Security Lake object.</p>"""
    transitions: NotRequired[
        "capo_securitylake.types.data_lake_lifecycle_transition_list.DataLakeLifecycleTransitionList"
    ]
    """<p>Provides data storage transition details of Amazon Security Lake object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeLifecycleConfiguration) -> dict:
    out: dict = {}
    if "expiration" in value:
        import capo_securitylake.types.data_lake_lifecycle_expiration

        out["expiration"] = (
            capo_securitylake.types.data_lake_lifecycle_expiration.serialize_json(
                value["expiration"]
            )
        )
    if "transitions" in value:
        import capo_securitylake.types.data_lake_lifecycle_transition_list

        out["transitions"] = (
            capo_securitylake.types.data_lake_lifecycle_transition_list.serialize_json(
                value["transitions"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataLakeLifecycleConfiguration:
    out: DataLakeLifecycleConfiguration = {}  # type: ignore[typeddict-item]
    if "expiration" in data:
        import capo_securitylake.types.data_lake_lifecycle_expiration

        out["expiration"] = (
            capo_securitylake.types.data_lake_lifecycle_expiration.deserialize_json(
                data["expiration"]
            )
        )
    if "transitions" in data:
        import capo_securitylake.types.data_lake_lifecycle_transition_list

        out["transitions"] = (
            capo_securitylake.types.data_lake_lifecycle_transition_list.deserialize_json(
                data["transitions"]
            )
        )
    return out
