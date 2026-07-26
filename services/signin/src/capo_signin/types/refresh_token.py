"""Generated from Smithy shape ``com.amazonaws.signin#RefreshToken``."""

from typing import TypeAlias

"""Encrypted refresh token with cnf.jkt This is the encrypted refresh token returned from auth code redemption. The token content includes cnf.jkt (SHA-256 thumbprint of the presented jwk). Used in subsequent token refresh requests."""
RefreshToken: TypeAlias = str
