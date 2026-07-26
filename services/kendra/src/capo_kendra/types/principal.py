"""Generated from Smithy shape ``com.amazonaws.kendra#Principal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.data_source_id
    import capo_kendra.types.principal_name
    import capo_kendra.types.principal_type
    import capo_kendra.types.read_access_type


class Principal(TypedDict, closed=True):
    name: "capo_kendra.types.principal_name.PrincipalName"
    """<p>The name of the user or group.</p>"""
    type: "capo_kendra.types.principal_type.PrincipalType"
    """<p>The type of principal.</p>"""
    access: "capo_kendra.types.read_access_type.ReadAccessType"
    """<p>Whether to allow or deny document access to the principal.</p>"""
    data_source_id: NotRequired["capo_kendra.types.data_source_id.DataSourceId"]
    """<p>The identifier of the data source the principal should access documents from.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Principal) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_kendra.types.principal_type

    out["Type"] = capo_kendra.types.principal_type.serialize_aws_json_1_1(value["type"])
    import capo_kendra.types.read_access_type

    out["Access"] = capo_kendra.types.read_access_type.serialize_aws_json_1_1(
        value["access"]
    )
    if "data_source_id" in value:
        out["DataSourceId"] = value["data_source_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Principal:
    out: Principal = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Principal.name required")
    if "Type" in data:
        import capo_kendra.types.principal_type

        out["type"] = capo_kendra.types.principal_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        raise DeserializationError("Principal.type required")
    if "Access" in data:
        import capo_kendra.types.read_access_type

        out["access"] = capo_kendra.types.read_access_type.deserialize_aws_json_1_1(
            data["Access"]
        )
    else:
        raise DeserializationError("Principal.access required")
    if "DataSourceId" in data:
        out["data_source_id"] = data["DataSourceId"]
    return out
