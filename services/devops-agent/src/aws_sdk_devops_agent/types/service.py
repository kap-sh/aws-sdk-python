"""Generated from Smithy shape ``com.amazonaws.devopsagent#Service``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>Enumeration of all supported service types, combining OAuth 3-legged, client credentials, and simple token authentication methods.</p>"""
Service: TypeAlias = Literal[
    "github",
    "slack",
    "azure",
    "azuredevops",
    "dynatrace",
    "servicenow",
    "pagerduty",
    "gitlab",
    "eventChannel",
    "mcpservernewrelic",
    "mcpservergrafana",
    "mcpserverdatadog",
    "mcpserver",
    "mcpserversplunk",
    "azureidentity",
    "mcpserversigv4",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "github",
        "slack",
        "azure",
        "azuredevops",
        "dynatrace",
        "servicenow",
        "pagerduty",
        "gitlab",
        "eventChannel",
        "mcpservernewrelic",
        "mcpservergrafana",
        "mcpserverdatadog",
        "mcpserver",
        "mcpserversplunk",
        "azureidentity",
        "mcpserversigv4",
    )
)


def serialize_json(value: Service) -> str:
    return value


def deserialize_json(data: str) -> Service:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Service value: {data!r}")
    return cast(Service, data)
