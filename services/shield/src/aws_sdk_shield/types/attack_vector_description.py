"""Generated from Smithy shape ``com.amazonaws.shield#AttackVectorDescription``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_shield.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_shield.types.string


class AttackVectorDescription(TypedDict):
    vector_type: "aws_sdk_shield.types.string.String"
    """<p>The attack type. Valid values:</p> <ul> <li> <p>UDP_TRAFFIC</p> </li> <li> <p>UDP_FRAGMENT</p> </li> <li> <p>GENERIC_UDP_REFLECTION</p> </li> <li> <p>DNS_REFLECTION</p> </li> <li> <p>NTP_REFLECTION</p> </li> <li> <p>CHARGEN_REFLECTION</p> </li> <li> <p>SSDP_REFLECTION</p> </li> <li> <p>PORT_MAPPER</p> </li> <li> <p>RIP_REFLECTION</p> </li> <li> <p>SNMP_REFLECTION</p> </li> <li> <p>MSSQL_REFLECTION</p> </li> <li> <p>NET_BIOS_REFLECTION</p> </li> <li> <p>SYN_FLOOD</p> </li> <li> <p>ACK_FLOOD</p> </li> <li> <p>REQUEST_FLOOD</p> </li> <li> <p>HTTP_REFLECTION</p> </li> <li> <p>UDS_REFLECTION</p> </li> <li> <p>MEMCACHED_REFLECTION</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttackVectorDescription) -> dict:
    out: dict = {}
    out["VectorType"] = value["vector_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttackVectorDescription:
    out: AttackVectorDescription = {}  # type: ignore[typeddict-item]
    if "VectorType" in data:
        out["vector_type"] = data["VectorType"]
    else:
        raise DeserializationError("AttackVectorDescription.vector_type required")
    return out
