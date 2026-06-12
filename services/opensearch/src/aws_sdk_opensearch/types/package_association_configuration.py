"""Generated from Smithy shape ``com.amazonaws.opensearch#PackageAssociationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.key_store_access_option


class PackageAssociationConfiguration(TypedDict):
    key_store_access_option: NotRequired[
        "aws_sdk_opensearch.types.key_store_access_option.KeyStoreAccessOption"
    ]
    """<p>The configuration parameters to enable accessing the key store required by the package.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageAssociationConfiguration) -> dict:
    out: dict = {}
    if "key_store_access_option" in value:
        import aws_sdk_opensearch.types.key_store_access_option

        out["KeyStoreAccessOption"] = (
            aws_sdk_opensearch.types.key_store_access_option.serialize_json(
                value["key_store_access_option"]
            )
        )
    return out


def deserialize_json(data: dict) -> PackageAssociationConfiguration:
    out: PackageAssociationConfiguration = {}  # type: ignore[typeddict-item]
    if "KeyStoreAccessOption" in data:
        import aws_sdk_opensearch.types.key_store_access_option

        out["key_store_access_option"] = (
            aws_sdk_opensearch.types.key_store_access_option.deserialize_json(
                data["KeyStoreAccessOption"]
            )
        )
    return out
