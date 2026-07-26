"""Generated from Smithy shape ``com.amazonaws.securityagent#RiskType``."""

from typing import Literal, TypeAlias, cast

"""<p>Type of security risk.</p>"""
RiskType: TypeAlias = Literal[
    "CROSS_SITE_SCRIPTING",
    "DEFAULT_CREDENTIALS",
    "INSECURE_DIRECT_OBJECT_REFERENCE",
    "PRIVILEGE_ESCALATION",
    "SERVER_SIDE_TEMPLATE_INJECTION",
    "COMMAND_INJECTION",
    "CODE_INJECTION",
    "SQL_INJECTION",
    "ARBITRARY_FILE_UPLOAD",
    "INSECURE_DESERIALIZATION",
    "LOCAL_FILE_INCLUSION",
    "INFORMATION_DISCLOSURE",
    "PATH_TRAVERSAL",
    "SERVER_SIDE_REQUEST_FORGERY",
    "JSON_WEB_TOKEN_VULNERABILITIES",
    "XML_EXTERNAL_ENTITY",
    "FILE_DELETION",
    "OTHER",
    "GRAPHQL_VULNERABILITIES",
    "BUSINESS_LOGIC_VULNERABILITIES",
    "CRYPTOGRAPHIC_VULNERABILITIES",
    "DENIAL_OF_SERVICE",
    "FILE_ACCESS",
    "FILE_CREATION",
    "DATABASE_MODIFICATION",
    "DATABASE_ACCESS",
    "OUTBOUND_SERVICE_REQUEST",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: RiskType) -> str:
    return value


def deserialize_json(data: str) -> RiskType:
    return cast(RiskType, data)
