"""Generated from Smithy shape ``com.amazonaws.workspacesweb#Event``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_web.errors import DeserializationError

Event: TypeAlias = Literal[
    "WebsiteInteract",
    "FileDownloadFromSecureBrowserToRemoteDisk",
    "FileTransferFromRemoteToLocalDisk",
    "FileTransferFromLocalToRemoteDisk",
    "FileUploadFromRemoteDiskToSecureBrowser",
    "ContentPasteToWebsite",
    "ContentTransferFromLocalToRemoteClipboard",
    "ContentCopyFromWebsite",
    "UrlLoad",
    "TabOpen",
    "TabClose",
    "PrintJobSubmit",
    "SessionConnect",
    "SessionStart",
    "SessionDisconnect",
    "SessionEnd",
    "UrlBlockByContentFilter",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WebsiteInteract",
        "FileDownloadFromSecureBrowserToRemoteDisk",
        "FileTransferFromRemoteToLocalDisk",
        "FileTransferFromLocalToRemoteDisk",
        "FileUploadFromRemoteDiskToSecureBrowser",
        "ContentPasteToWebsite",
        "ContentTransferFromLocalToRemoteClipboard",
        "ContentCopyFromWebsite",
        "UrlLoad",
        "TabOpen",
        "TabClose",
        "PrintJobSubmit",
        "SessionConnect",
        "SessionStart",
        "SessionDisconnect",
        "SessionEnd",
        "UrlBlockByContentFilter",
    )
)


def serialize_json(value: Event) -> str:
    return value


def deserialize_json(data: str) -> Event:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Event value: {data!r}")
    return cast(Event, data)
