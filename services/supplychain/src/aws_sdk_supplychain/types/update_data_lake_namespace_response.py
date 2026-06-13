"""Generated from Smithy shape ``com.amazonaws.supplychain#UpdateDataLakeNamespaceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_lake_namespace


class UpdateDataLakeNamespaceResponse(TypedDict):
    namespace: "aws_sdk_supplychain.types.data_lake_namespace.DataLakeNamespace"
    """<p>The updated namespace details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataLakeNamespaceResponse) -> dict:
    out: dict = {}
    import aws_sdk_supplychain.types.data_lake_namespace

    out["namespace"] = aws_sdk_supplychain.types.data_lake_namespace.serialize_json(
        value["namespace"]
    )
    return out


def deserialize_json(data: dict) -> UpdateDataLakeNamespaceResponse:
    out: UpdateDataLakeNamespaceResponse = {}  # type: ignore[typeddict-item]
    if "namespace" in data:
        import aws_sdk_supplychain.types.data_lake_namespace

        out["namespace"] = (
            aws_sdk_supplychain.types.data_lake_namespace.deserialize_json(
                data["namespace"]
            )
        )
    else:
        raise DeserializationError("UpdateDataLakeNamespaceResponse.namespace required")
    return out
